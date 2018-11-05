#include <iostream>
#include <functional>

#include "../include/game.h"
#include "../include/utilities.h"


void add_player(Game& game)
{
    auto name {util::ask_for_string("Player Name?")};
    int cards {util::ask_for_int("Number of Cards?", 1, game.get_remaining_cards())};
    game.add_player(name, cards);
}

void set_active(Game& game)
{
    auto players {game.get_players()};
    if (players.empty())
    {
        std::cout << "Add more players!" << std::endl;
        return;
    }
    auto names {util::list_string(players, [](auto& player){return player->name;})};
    int active_player {util::ask_for_int("Select the active player:\n" + names, 1, static_cast<int>(players.size()))};
    auto it {players.begin()};
    std::advance(it, active_player - 1);
    game.set_active_player(**it);
}

void add_guess(Game& game)
{
    auto players {game.get_players()};
    if (players.size() < 2)
    {
        std::cout << "Add more m_players!" << std::endl;
        return;
    }
    int guesser {util::ask_for_int("Select the guessing player:\n"
                                   + util::list_string(players, [](auto& player){return player->name;}),
                                   1, static_cast<int>(players.size()))};
    int person {util::ask_for_int("Select the murderer\n" + util::list_string(game.deck.people),
                                  1, static_cast<int>(game.deck.people.size()))};
    int weapon {util::ask_for_int("Select the weapon\n" + util::list_string(game.deck.weapons),
                                  1, static_cast<int>(game.deck.weapons.size()))};
    int room {util::ask_for_int("Select the room\n" + util::list_string(game.deck.rooms),
                                1, static_cast<int>(game.deck.rooms.size()))};
    std::string prompt {"Select the answering player:\n0. No one\n"};
    std::vector<int> options;
    int index {1};
    for(auto& player: players)
    {
        if (index != guesser)
        {
            options.push_back(index);
            prompt += std::to_string(index);
            prompt += ". ";
            prompt += player->name;
            if (index != static_cast<int>(players.size()))
            {
                prompt += "\n";
            }
        }
        index++;
    }
    int answerer {util::ask_for_int(prompt, [&](int val)
    {
        return val >= 0 and val <= static_cast<int>(players.size()) and val != guesser;
    })};
    const Card* card {nullptr};
    auto guess_it {players.begin()};
    std::advance(guess_it, guesser - 1);
    const Player* answerer_ptr {nullptr};
    if(answerer != 0)
    {
        auto answer_it {players.end()};
        std::advance(answer_it, answerer - 1);
        answerer_ptr = *answer_it;
    }
    if (*guess_it == game.get_active_player())
    {
        std::vector<const Card*> cards;
        cards.push_back(&game.deck.people[person - 1]);
        cards.push_back(&game.deck.weapons[weapon - 1]);
        cards.push_back(&game.deck.rooms[room - 1]);
        int choice {util::ask_for_int("Select the card shown:\n"
                                      + util::list_string(cards, [](auto& card){return card->name;}),
                                      1, static_cast<int>(cards.size()))};
        card = cards[choice - 1];
    }
    game.add_guess(**guess_it,
                   answerer_ptr,
                   {},
                   game.deck.people[person - 1],
                   game.deck.weapons[weapon - 1],
                   game.deck.rooms[room - 1], card);
}

void view_guesses(Game& game)
{
    std::string prompt {"Guesses:\n" + util::list_string(game.get_guesses(), [&](Guess& guess)
    {
        std::string response {guess.guesser.name + ": ("
               + guess.murderer.name + ", "
               + guess.weapon.name + ", "
               + guess.room.name + ")"};
        if (guess.answerer)
        {
            response += ", " + guess.answerer->name;
        }
        if (guess.answer)
        {
            response += ": " + guess.answer->name;
        }
        if (!guess.skipped_players.empty())
        {
            response += ", Skipped: {";
            for (auto& player: guess.skipped_players)
            {
                response += player->name + ",";
            }
            response += "}";
        }
        return response;
    })};
    std::cout << prompt << std::endl;
}

void analyze(Game& game)
{
    if (game.get_players().empty())
    {
        std::cout << "Add more players!" << std::endl;
        return;
    }
    for(auto& [player, stat]: game.analyzer.get_stats())
    {
        std::cout << player->name << ":" << std::endl;
        std::cout << "\tHas: ";
        for (auto& card: stat.positives)
        {
            std::cout << card->name << ", ";
        }
        std::cout << std::endl;

        std::cout << "\tDoesn't have: ";
        for (auto& card: stat.negatives)
        {
            std::cout << card->name << ", ";
        }

        std::cout << std::endl;

    }
}

int main()
{
    Game game;
    std::string prompt {"0. Exit\n1. Add Player\n2. Set Active Player\n3. Add Guess\n4. View Guesses\n5. Analyze"};

    std::map<int, std::function<void(Game&)>> function_map
    {
        {1, add_player},
        {2, set_active},
        {3, add_guess},
        {4, view_guesses},
        {5, analyze}
    };
    while (true)
    {
        int option {util::ask_for_int(prompt, 0, 5)};
        if (option == 0)
        {
            break;
        } else {
            function_map[option](game);
        }
    }
    std::cout << "Game Ending" << std::endl;
    std::cout << "Players(" << game.get_players().size() << "):" << std::endl;
    for (const auto& player: game.get_players())
    {
        std::cout << "  " << player->name << ": " << player->num_cards << std::endl;
    }
    return 0;
}