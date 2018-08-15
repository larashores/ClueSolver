#include "python/py_guess.h"

namespace python {

const Player& guesser(Guess& guess) { return guess.guesser; }
const Player* answerer(Guess& guess) { return guess.answerer; }
const Person& murderer(Guess& guess) { return guess.murderer; }
const Weapon& weapon(Guess& guess) { return guess.weapon; }
const Room& room(Guess& guess) { return guess.room; }
const Card* answer(Guess& guess) { return guess.answer; }

}  // namespace