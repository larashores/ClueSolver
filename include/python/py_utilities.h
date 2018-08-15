#pragma once

#include <boost/python.hpp>

namespace python {

template<typename Sequence>
boost::python::list stl2py(const Sequence& sequence)
{
    boost::python::list list;
    for(auto& arg: sequence)
    {
        list.append(arg);
    }
    return list;
}

template<typename Sequence>
boost::python::list stl2pyptr(Sequence sequence)
{
    boost::python::list list;
    for(auto& arg: sequence)
    {
        list.append(&arg);
    }
    return list;
}

}  // namespace