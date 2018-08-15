#include "python/py_analyzer.h"

namespace PY = boost::python;

namespace python {

    PY::dict get_stats(const Analyzer& analyzer)
    {
        PY::dict dict;
        auto stat_map {analyzer.get_stats()};
        for(auto& pair: stat_map)
        {
            dict[pair.first] = pair.second;
        }
    }

}  // namespace python