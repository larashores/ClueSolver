#include "python/cards/py_deck.h"
#include "python/py_utilities.h"

namespace PY = boost::python;

namespace python {

PY::list people(Deck& deck)
{
    return stl2pyptr(deck.people);
}

PY::list weapons(Deck& deck)
{
    return stl2pyptr(deck.weapons);
}

PY::list rooms(Deck& deck)
{
    return stl2pyptr(deck.rooms);
}

}  // namespace