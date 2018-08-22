#include "python/py_analyzer.h"
#include "python/py_utilities.h"

namespace PY = boost::python;

namespace python {

    PY::dict get_stats(const Analyzer& analyzer)
    {
        PY::dict dict;
        auto stat_map {analyzer.get_stats()};
        for(auto& pair: stat_map)
        {
            dict[to_shared_ptr(*pair.first)] = pair.second;
        }
        return dict;
    }

}  // namespace python