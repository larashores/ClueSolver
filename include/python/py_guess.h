#pragma once

#include "guess.h"

namespace python {

const Player& guesser(Guess& guess);
const Player* answerer(Guess& guess);
const Person& murderer(Guess& guess);
const Weapon& weapon(Guess& guess);
const Room& room(Guess& guess);
const Card* answer(Guess& guess);

}  // namespace