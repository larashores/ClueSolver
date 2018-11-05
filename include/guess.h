#pragma once

#include <vector>

#include "player.h"
#include "cards/person.h"
#include "cards/weapon.h"
#include "cards/room.h"


struct Guess
{
    Guess(const Player& guesser, const Player* answerer,
          const Person& murderer, const Weapon& weapon, const Room& room,
          const std::vector<Player*>& skipped, const Card* answer);

    const Player& guesser;
    const Player* answerer;
    const Person& murderer;
    const Weapon& weapon;
    const Room& room;
    const Card* answer;
    std::vector<Player*> skipped_players;
    
    explicit operator std::string() const;
};
