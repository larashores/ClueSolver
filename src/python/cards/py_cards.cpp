#include "python/cards/py_cards.h"
#include "python/py_utilities.h"


std::ostream& operator<<(std::ostream& stream, const Card& card)
{
    return stream << std::string{card};
}

bool operator==(const Card& card1, const Card& card2)
{
    return &card1 == &card2;
}