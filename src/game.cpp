#include <algorithm>

#include "../include/game.h"
#include "../include/utilities.h"

using namespace std::literals;


Game::Game() :
    analyzer{*this}
{

}

void Game::add_player(const std::string& name, int num_cards)
{
    int remaining {get_remaining_cards()};
    num_cards = num_cards > remaining ? remaining : num_cards;
    m_players.emplace_back(name, num_cards);
}

void Game::add_guess(const Player& guessor, const Player* answerer,
                     const Person& murderer, const Weapon& weapon, const Room& room,
                     const Card* card)
{
    std::vector<Player*> dont_haves;
    if (answerer)
    {
        auto it {std::find_if(m_players.begin(), m_players.end(), [&](Player& player){return &player == &guessor;})};
        while (true)
        {
            it++;
            it = it == m_players.end() ? m_players.begin() : it;
            if (&(*it) != &guessor and &(*it) != answerer)
            {
                dont_haves.push_back(&*(it));
            } else
            {
                break;
            }
        }
    }
    m_guesses.emplace_back(guessor, answerer, murderer, weapon, room, dont_haves, card);
}

void Game::set_active_player(const Player& player)
{
    m_active_player = &player;
}

const Player* Game::get_active_player() const
{
    return m_active_player;
}

const std::vector<Guess> Game::get_guesses() const
{
    return m_guesses;
}

const std::list<Player>& Game::get_const_players() const
{
    return m_players;
}

std::vector<Player*> Game::get_players()
{
    std::vector<Player*> vec (m_players.size());
    std::transform(m_players.begin(), m_players.end(), vec.begin(), [](auto& player){return &player;});
    return vec;
}

int Game::get_remaining_cards() const
{
    int start {deck.size()};
    for (auto& player: m_players)
    {
        start -= player.num_cards;
    }
    return start;
}
