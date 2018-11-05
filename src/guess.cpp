#include <iostream>
#include "../include/guess.h"

#include <sstream>

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

Guess::operator std::string() const
{
    std::ostringstream stream;
    stream << "Guesser: " << guesser.name << ", Answerer: " << (answerer ? answerer->name : "Nobody")
           << ", Murderer: " << murderer.name << ", Weapon: " << weapon.name << ", Room: " << room.name;
    if (answer)
    {
        stream << ", Card Shown: " << answer->name;
    }
    stream << ", Skipped Players: [";
    for (auto& player: skipped_players)
    {
        stream << player->name << ", ";
    }
    stream << "]";
    return stream.str();
}