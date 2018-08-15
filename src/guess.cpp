#include <iostream>
#include "../include/guess.h"


Guess::Guess(const Player& guesser_, const Player* answerer_,
             const Person& murderer_, const Weapon& weapon_, const Room& room_,
             const std::vector<Player*>& skipped, const Card* answer_) :
        guesser{guesser_},
        answerer{answerer_},
        murderer{murderer_},
        weapon{weapon_},
        room{room_},
        answer{answer_},
        skipped_players{skipped}
{
}
