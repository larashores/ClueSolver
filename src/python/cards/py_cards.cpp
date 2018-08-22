#include "python/cards/py_cards.h"


std::ostream& operator<<(std::ostream& stream, const Card& card)
{
    return stream << std::string{card};
}

bool operator==(const Card& card1, const Card& card2)
{
    return &card1 == &card2;
}

namespace python {

    long hash_card(const Card& card) {
        return reinterpret_cast<uintptr_t>(&card) / 8;
    }

}  // namespace python
