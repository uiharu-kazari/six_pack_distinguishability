# Notes

getting the ladder length (filtration value) when a simplex appears:
```python
alpha_complex.weight_function
```

`chro.ChromaticAlphaComplex` computes the chromatic alpha complex of a point cloud. Which is not required if we start directly from a simplicial complex.

See the "# Define your own simplicial complex" section in the manual for more details.

Only constant remove is allowed.

all simplices
```python
alpha_complex.simplices()
```

those from labelled as 0
```python
 alpha_complex.get_simplicial_complex(sub_complex='0')
```

those from labelled as 1
```python
 alpha_complex.get_simplicial_complex(sub_complex='1')
```
## TODOs

* Compute the 6-packs for the point cloud model.
~~See if we can combine them to make an indistinguishable example~~
* Just check the rank of the matrix.
* On the simplicial complex level.
* 5-packs for the point cloud model, at homology dimension 1.

## Slides

Three levels
* Topological space (Point cloud)
* Simplicial complex
* Persistence module / Representation



## Questions
```python
simplex
(26, 36, 126, 142)
# Get the labels of a given simplex
alpha_complex.simplex_labels(simplex)
{0, 1}
```
means the simplex involves points labelled with both 0 and 1?

Can I remove the (1,2) in the graph?
