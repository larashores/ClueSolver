#pragma once

#include <boost\python.hpp>

#include "analyzer.h"

namespace python
{

boost::python::dict get_stats(const Analyzer& analyzer);

}  // namespace python