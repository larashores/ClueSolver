#include "../include/analyzer.h"

#include "../include/game.h"

Analyzer::Analyzer(const Game& game) :
    m_game{game}
{
}

std::map<const Player*, Stats> Analyzer::get_stats() const
{
    std::map<const Player*, Stats> stats;
    for (auto& player: m_game.get_const_players())
    {
        stats.emplace(std::piecewise_construct,
                      std::make_tuple(&player),
                      std::make_tuple());
    }
    analyze_overrides(stats);
//    for (auto& guess: m_game.get_guesses())
//    {
//        if (guess.answer)
//        {
//            stats[guess.answerer].positives.insert(guess.answer);
//        }
//        for (auto& player: guess.skipped_players)
//        {
//            stats[player].negatives.insert(&guess.murderer);
//            stats[player].negatives.insert(&guess.weapon);
//            stats[player].negatives.insert(&guess.room);
//        }
//    }
    analyze_num_cards(stats);
//    analyze_negatives(stats);
    return stats;
}

void Analyzer::analyze_negatives(std::map<const Player *, Stats>& stats) const
{
    for (auto& guess: m_game.get_guesses())
    {
        if (not guess.answer) {
            auto &negatives{stats[guess.answerer].negatives};
            bool no_murderer{negatives.find(&guess.murderer) != negatives.end()};
            bool no_weapon{negatives.find(&guess.weapon) != negatives.end()};
            bool no_room{negatives.find(&guess.room) != negatives.end()};
            if (no_murderer and no_weapon and !no_room) {
                stats[guess.answerer].positives.insert(&guess.room);
            } else if (no_murderer and !no_weapon and no_room) {
                stats[guess.answerer].positives.insert(&guess.weapon);
            } else if (!no_murderer and no_weapon and no_room) {
                stats[guess.answerer].positives.insert(&guess.murderer);
            }
        }
    }
}

void Analyzer::analyze_overrides(std::map<const Player*, Stats>& stats) const
{

    for(auto& [player, cards]: m_game.positive_overrides)
    {
        auto& set {stats[player].positives};
        std::copy(cards.begin(), cards.end(), std::inserter(set, set.begin()));
        for(auto& player2: m_game.get_const_players())
        {
            if (&player2 != player)
            {
                auto& negative_set {stats[&player2].negatives};
                std::copy(cards.begin(), cards.end(), std::inserter(negative_set, negative_set.begin()));
            }
        }
    }
    for(auto& [player, cards]: m_game.negative_overrides)
    {
        auto& set {stats[player].negatives};
        std::copy(cards.begin(), cards.end(), std::inserter(set, set.begin()));
    }
}

void Analyzer::analyze_num_cards(std::map<const Player *, Stats> &stats) const
{
    for (auto& player: m_game.get_const_players())
    {
        auto& positives {stats[&player].positives};
        auto& negatives {stats[&player].negatives};
        if (static_cast<int>(positives.size()) >= player.num_cards)
        {
            for (auto& card: m_game.deck.get_all_cards())
            {
                if (positives.find(card) == positives.end())
                {
                    negatives.insert(card);
                }
            }
        }
    }
}

