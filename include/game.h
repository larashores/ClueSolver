#pragma once

#include <list>
#include <map>

#include "cards/deck.h"
#include "guess.h"
#include "player.h"
#include "stats.h"
#include "analyzer.h"
#include "override.h"

class Game
{
public:
    Game();

    void add_player(const std::string& name, int num_cards);
    void add_guess(const Player& guessor, const Player* answerer,
                   const Person& murderer, const Weapon& weapon, const Room& room,
                   const Card* card = nullptr);
    std::vector<Guess> get_guesses() const;
    const std::list<Player>& get_const_players() const;
    std::vector<Player*> get_players();
    int get_remaining_cards() const;

    void set_active_player(const Player& player);
    const Player* get_active_player() const;

    const Deck deck;
    const Analyzer analyzer;

    std::map<const Player*, std::map<const Card*, Override>> overrides;

private:
    const Player* m_active_player {nullptr};

    std::list<Player> m_players;
    std::vector<Guess> m_guesses;
};
