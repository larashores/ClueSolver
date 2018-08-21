#include "python/cards/py_deck.h"
#include "python/py_utilities.h"

namespace PY = boost::python;

namespace python {

PY::list people(Deck& deck)
{
    return to_ptr_list(deck.people);
}

PY::list weapons(Deck& deck)
{
    return to_ptr_list(deck.weapons);
}

PY::list rooms(Deck& deck)
{
    return to_ptr_list(deck.rooms);
}

}  // namespace