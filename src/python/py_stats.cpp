#include "python/py_stats.h"

#include "python/py_utilities.h"

namespace PY = boost::python;

namespace python
{
    PY::list positives(Stats& stats)
    {
        boost::python::list list;
        for(auto& arg: stats.positives)
        {
            list.append(to_shared_ptr(*arg));
        }
        return list;
    }

    PY::list negatives(Stats& stats)
    {
        boost::python::list list;
        for(auto& arg: stats.negatives)
        {
            list.append(to_shared_ptr(*arg));
        }
        return list;
    }
}
