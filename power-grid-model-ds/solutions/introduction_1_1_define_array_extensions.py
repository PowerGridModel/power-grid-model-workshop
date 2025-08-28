class MyNodeArray(NodeArray):
    _defaults = {"x": 0.0, "y": 0.0, "u": 0.0}
    x: NDArray[np.float64]
    y: NDArray[np.float64]
    u: NDArray[np.float64]

class MyLineArray(LineArray):
    _defaults = {"i_from": 0.0}
    i_from: NDArray[np.float64]