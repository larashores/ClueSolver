#include "python/py_stats.h"

#include "python/py_utilities.h"

namespace PY = boost::python;

namespace python
{
    PY::list positives(Stats& stats)
    {
        return stl2py(stats.positives);
    }

    PY::list negatives(Stats& stats)
    {
        return stl2py(stats.negatives);
    }
}
