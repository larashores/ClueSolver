#include "python/py_analyzer.h"
#include "python/py_utilities.h"

namespace PY = boost::python;

namespace python {

    PY::dict get_stats(const Analyzer& analyzer)
    {
        PY::dict dict;
        auto stat_map {analyzer.get_stats()};
        for(auto& [player, stats]: stat_map)
        {
            dict[to_shared_ptr(*player)] = stats;
        }
        return dict;
    }

}  // namespace python