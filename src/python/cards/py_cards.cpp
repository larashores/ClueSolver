#include "python/cards/py_cards.h"


std::ostream& operator<<(std::ostream& stream, const Card& card)
{
    return stream << std::string{card};
}