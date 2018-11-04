#pragma once

#include <boost/python.hpp>

#include "cards/deck.h"
#include "python/py_utilities.h"

namespace python { 
boost::python::list all_cards(Deck& deck);
boost::python::list people(Deck& deck);
boost::python::list weapons(Deck& deck);
boost::python::list rooms(Deck& deck);

}  // namespace