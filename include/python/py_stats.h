#pragma once

#include <boost/python.hpp>

#include "stats.h"

namespace python {

boost::python::list positives(Stats& stats);
boost::python::list negatives(Stats& stats);

}  // namespace