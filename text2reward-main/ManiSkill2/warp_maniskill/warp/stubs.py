# Autogenerated file, do not edit, this file provides stubs for builtins autocomplete in VSCode, PyCharm, etc

from typing import Any
from typing import Tuple
from typing import Callable
from typing import overload
from warp.types import array, array2d, array3d, array4d, constant
from warp.types import int8, uint8, int16, uint16, int32, uint32, int64, uint64, float16, float32, float64
from warp.types import vec2, vec3, vec4, mat22, mat33, mat44, quat, transform, spatial_vector, spatial_matrix
from warp.types import mesh_query_aabb_t, hash_grid_query_t


@overload
def min(x: int32, y: int32) -> int:
   """
   Return the minimum of two integers.
   """
   ...

@overload
def min(x: float32, y: float32) -> float:
   """
   Return the minimum of two floats.
   """
   ...

@overload
def max(x: int32, y: int32) -> int:
   """
   Return the maximum of two integers.
   """
   ...

@overload
def max(x: float32, y: float32) -> float:
   """
   Return the maximum of two floats.
   """
   ...

@overload
def clamp(x: int32, a: int32, b: int32) -> int:
   """
   Clamp the value of x to the range [a, b].
   """
   ...

@overload
def clamp(x: float32, a: float32, b: float32) -> float:
   """
   Clamp the value of x to the range [a, b].
   """
   ...

@overload
def abs(x: int32) -> int:
   """
   Return the absolute value of x.
   """
   ...

@overload
def abs(x: float32) -> float:
   """
   Return the absolute value of x.
   """
   ...

@overload
def sign(x: int32) -> int:
   """
   Return -1 if x < 0, return 1 otherwise.
   """
   ...

@overload
def sign(x: float32) -> float:
   """
   Return -1.0 if x < 0.0, return 1.0 otherwise.
   """
   ...

@overload
def step(x: float32) -> float:
   """
   Return 1.0 if x < 0.0, return 0.0 otherwise.
   """
   ...

@overload
def nonzero(x: float32) -> float:
   """
   Return 1.0 if x is not equal to zero, return 0.0 otherwise.
   """
   ...

@overload
def sin(x: float32) -> float:
   """
   Return the sine of x in radians.
   """
   ...

@overload
def cos(x: float32) -> float:
   """
   Return the cosine of x in radians.
   """
   ...

@overload
def acos(x: float32) -> float:
   """
   Return arccos of x in radians. Inputs are automatically clamped to [-1.0, 1.0].
   """
   ...

@overload
def asin(x: float32) -> float:
   """
   Return arcsin of x in radians. Inputs are automatically clamped to [-1.0, 1.0].
   """
   ...

@overload
def sqrt(x: float32) -> float:
   """
   Return the sqrt of x, where x is positive.
   """
   ...

@overload
def tan(x: float32) -> float:
   """
   Return tangent of x in radians.
   """
   ...

@overload
def atan(x: float32) -> float:
   """
   Return arctan of x.
   """
   ...

@overload
def atan2(y: float32, x: float32) -> float:
   """
   Return atan2 of x.
   """
   ...

@overload
def sinh(x: float32) -> float:
   """
   Return the sinh of x.
   """
   ...

@overload
def cosh(x: float32) -> float:
   """
   Return the cosh of x.
   """
   ...

@overload
def tanh(x: float32) -> float:
   """
   Return the tanh of x.
   """
   ...

@overload
def log(x: float32) -> float:
   """
   Return the natural log (base-e) of x, where x is positive.
   """
   ...

@overload
def log2(x: float32) -> float:
   """
   Return the natural log (base-2) of x, where x is positive.
   """
   ...

@overload
def log10(x: float32) -> float:
   """
   Return the natural log (base-10) of x, where x is positive.
   """
   ...

@overload
def exp(x: float32) -> float:
   """
   Return base-e exponential, e^x.
   """
   ...

@overload
def pow(x: float32, y: float32) -> float:
   """
   Return the result of x raised to power of y.
   """
   ...

@overload
def round(x: float32) -> float:
   """
   Calculate the nearest integer value, rounding halfway cases away from zero.
      This is the most intuitive form of rounding in the colloquial sense, but can be slower than other options like ``warp.rint()``.
      Differs from ``numpy.round()``, which behaves the same way as ``numpy.rint()``.
   """
   ...

@overload
def rint(x: float32) -> float:
   """
   Calculate the nearest integer value, rounding halfway cases to nearest even integer.
      It is generally faster than ``warp.round()``.
      Equivalent to ``numpy.rint()``.
   """
   ...

@overload
def trunc(x: float32) -> float:
   """
   Calculate the nearest integer that is closer to zero than x.
      In other words, it discards the fractional part of x.
      It is similar to casting ``float(int(x))``, but preserves the negative sign when x is in the range [-0.0, -1.0).
      Equivalent to ``numpy.trunc()`` and ``numpy.fix()``.
   """
   ...

@overload
def floor(x: float32) -> float:
   """
   Calculate the largest integer that is less than or equal to x.
   """
   ...

@overload
def ceil(x: float32) -> float:
   """
   Calculate the smallest integer that is greater than or equal to x.
   """
   ...

@overload
def dot(x: vec2, y: vec2) -> float:
   """
   Compute the dot product between two 2d vectors.
   """
   ...

@overload
def dot(x: vec3, y: vec3) -> float:
   """
   Compute the dot product between two 3d vectors.
   """
   ...

@overload
def dot(x: vec4, y: vec4) -> float:
   """
   Compute the dot product between two 4d vectors.
   """
   ...

@overload
def dot(x: quat, y: quat) -> float:
   """
   Compute the dot product between two quaternions.
   """
   ...

@overload
def outer(x: vec2, y: vec2) -> mat22:
   """
   Compute the outer product x*y^T for two vec2 objects.
   """
   ...

@overload
def outer(x: vec3, y: vec3) -> mat33:
   """
   Compute the outer product x*y^T for two vec3 objects.
   """
   ...

@overload
def cross(x: vec3, y: vec3) -> vec3:
   """
   Compute the cross product of two 3d vectors.
   """
   ...

@overload
def skew(x: vec3) -> mat33:
   """
   Compute the skew symmetric matrix for a 3d vector.
   """
   ...

@overload
def length(x: vec2) -> float:
   """
   Compute the length of a 2d vector.
   """
   ...

@overload
def length(x: vec3) -> float:
   """
   Compute the length of a 3d vector.
   """
   ...

@overload
def length(x: vec4) -> float:
   """
   Compute the length of a 4d vector.
   """
   ...

@overload
def normalize(x: vec2) -> vec2:
   """
   Compute the normalized value of x, if length(x) is 0 then the zero vector is returned.
   """
   ...

@overload
def normalize(x: vec3) -> vec3:
   """
   Compute the normalized value of x, if length(x) is 0 then the zero vector is returned.
   """
   ...

@overload
def normalize(x: vec4) -> vec4:
   """
   Compute the normalized value of x, if length(x) is 0 then the zero vector is returned.
   """
   ...

@overload
def normalize(x: quat) -> quat:
   """
   Compute the normalized value of x, if length(x) is 0 then the zero quat is returned.
   """
   ...

@overload
def transpose(m: mat22) -> mat22:
   """
   Return the transpose of the matrix m
   """
   ...

@overload
def transpose(m: mat33) -> mat33:
   """
   Return the transpose of the matrix m
   """
   ...

@overload
def transpose(m: mat44) -> mat44:
   """
   Return the transpose of the matrix m
   """
   ...

@overload
def transpose(m: spatial_matrix) -> spatial_matrix:
   """
   Return the transpose of the matrix m
   """
   ...

@overload
def inverse(m: mat22) -> mat22:
   """
   Return the inverse of the matrix m
   """
   ...

@overload
def inverse(m: mat33) -> mat33:
   """
   Return the inverse of the matrix m
   """
   ...

@overload
def inverse(m: mat44) -> mat44:
   """
   Return the inverse of the matrix m
   """
   ...

@overload
def determinant(m: mat22) -> float:
   """
   Return the determinant of the matrix m
   """
   ...

@overload
def determinant(m: mat33) -> float:
   """
   Return the determinant of the matrix m
   """
   ...

@overload
def determinant(m: mat44) -> float:
   """
   Return the determinant of the matrix m
   """
   ...

@overload
def diag(d: vec2) -> mat22:
   """
   Returns a matrix with the components of the vector d on the diagonal
   """
   ...

@overload
def diag(d: vec3) -> mat33:
   """
   Returns a matrix with the components of the vector d on the diagonal
   """
   ...

@overload
def diag(d: vec4) -> mat44:
   """
   Returns a matrix with the components of the vector d on the diagonal
   """
   ...

@overload
def cw_mul(x: vec2, y: vec2) -> vec2:
   """
   Component wise multiply of two 2d vectors.
   """
   ...

@overload
def cw_mul(x: vec3, y: vec3) -> vec3:
   """
   Component wise multiply of two 3d vectors.
   """
   ...

@overload
def cw_mul(x: vec4, y: vec4) -> vec4:
   """
   Component wise multiply of two 4d vectors.
   """
   ...

@overload
def cw_div(x: vec2, y: vec2) -> vec2:
   """
   Component wise division of two 2d vectors.
   """
   ...

@overload
def cw_div(x: vec3, y: vec3) -> vec3:
   """
   Component wise division of two 3d vectors.
   """
   ...

@overload
def cw_div(x: vec4, y: vec4) -> vec4:
   """
   Component wise division of two 4d vectors.
   """
   ...

@overload
def svd3(A: mat33, U: mat33, sigma: vec3, V: mat33):
   """
   Compute the SVD of a 3x3 matrix. The singular values are returned in sigma, 
      while the left and right basis vectors are returned in U and V.
   """
   ...

@overload
def quat_identity() -> quat:
   """
   Construct an identity quaternion with zero imaginary part and real part of 1.0
   """
   ...

@overload
def quat_from_axis_angle(axis: vec3, angle: float32) -> quat:
   """
   Construct a quaternion representing a rotation of angle radians around the given axis.
   """
   ...

@overload
def quat_from_matrix(m: mat33) -> quat:
   """
   Construct a quaternion from a 3x3 matrix.
   """
   ...

@overload
def quat_rpy(roll: float32, pitch: float32, yaw: float32) -> quat:
   """
   Construct a quaternion representing a combined roll (z), pitch (x), yaw rotations (y) in radians.
   """
   ...

@overload
def quat_inverse(q: quat) -> quat:
   """
   Compute quaternion conjugate.
   """
   ...

@overload
def quat_rotate(q: quat, p: vec3) -> vec3:
   """
   Rotate a vector by a quaternion.
   """
   ...

@overload
def quat_rotate_inv(q: quat, p: vec3) -> vec3:
   """
   Rotate a vector the inverse of a quaternion.
   """
   ...

@overload
def quat_to_matrix(q: quat) -> mat33:
   """
   Convert a quaternion to a 3x3 rotation matrix.
   """
   ...

@overload
def transform_identity() -> transform:
   """
   Construct an identity transform with zero translation and identity rotation.
   """
   ...

@overload
def transform_get_translation(t: transform) -> vec3:
   """
   Return the translational part of a transform.
   """
   ...

@overload
def transform_get_rotation(t: transform) -> quat:
   """
   Return the rotational part of a transform.
   """
   ...

@overload
def transform_multiply(a: transform, b: transform) -> transform:
   """
   Multiply two rigid body transformations together.
   """
   ...

@overload
def transform_point(t: transform, p: vec3) -> vec3:
   """
   Apply the transform to a point p treating the homogenous coordinate as w=1 (translation and rotation).
   """
   ...

@overload
def transform_point(m: mat44, p: vec3) -> vec3:
   """
   Apply the transform to a point ``p`` treating the homogenous coordinate as w=1. The transformation is applied treating ``p`` as a column vector, e.g.: ``y = M*p``
      note this is in contrast to some libraries, notably USD, which applies transforms to row vectors, ``y^T = p^T*M^T``. If the transform is coming from a library that uses row-vectors
      then users should transpose the tranformation matrix before calling this method.
   """
   ...

@overload
def transform_vector(t: transform, v: vec3) -> vec3:
   """
   Apply the transform to a vector v treating the homogenous coordinate as w=0 (rotation only).
   """
   ...

@overload
def transform_vector(m: mat44, v: vec3) -> vec3:
   """
   Apply the transform to a vector ``v`` treating the homogenous coordinate as w=0. The transformation is applied treating ``v`` as a column vector, e.g.: ``y = M*v``
      note this is in contrast to some libraries, notably USD, which applies transforms to row vectors, ``y^T = v^T*M^T``. If the transform is coming from a library that uses row-vectors
      then users should transpose the tranformation matrix before calling this method.
   """
   ...

@overload
def transform_inverse(t: transform) -> transform:
   """
   Compute the inverse of the transform.
   """
   ...

@overload
def spatial_dot(a: spatial_vector, b: spatial_vector) -> float:
   """
   Compute the dot product of two 6d screw vectors.
   """
   ...

@overload
def spatial_cross(a: spatial_vector, b: spatial_vector) -> spatial_vector:
   """
   Compute the cross-product of two 6d screw vectors.
   """
   ...

@overload
def spatial_cross_dual(a: spatial_vector, b: spatial_vector) -> spatial_vector:
   """
   Compute the dual cross-product of two 6d screw vectors.
   """
   ...

@overload
def spatial_top(a: spatial_vector) -> vec3:
   """
   Return the top (first) part of a 6d screw vector.
   """
   ...

@overload
def spatial_bottom(a: spatial_vector) -> vec3:
   """
   Return the bottom (second) part of a 6d screw vector.
   """
   ...

@overload
def spatial_jacobian(S: array[spatial_vector], joint_parents: array[int32], joint_qd_start: array[int32], joint_start: int32, joint_count: int32, J_start: int32, J_out: array[float32]):
   """

   """
   ...

@overload
def spatial_mass(I_s: array[spatial_matrix], joint_start: int32, joint_count: int32, M_start: int32, M: array[float32]):
   """

   """
   ...

@overload
def mlp(weights: array[float32], bias: array[float32], activation: Callable, index: int32, x: array[float32], out: array[float32]):
   """
   Evaluate a multi-layer perceptron (MLP) layer in the form: ``out = act(weights*x + bias)``. 

      :param weights: A layer's network weights with dimensions ``(m, n)``.
      :param bias: An array with dimensions ``(n)``.
      :param activation: A ``wp.func`` function that takes a single scalar float as input and returns a scalar float as output
      :param index: The batch item to process, typically each thread will process 1 item in the batch, in this case index should be ``wp.tid()``
      :param x: The feature matrix with dimensions ``(n, b)``
      :param out: The network output with dimensions ``(m, b)``

      :note: Feature and output matrices are transposed compared to some other frameworks such as PyTorch. All matrices are assumed to be stored in flattened row-major memory layout (NumPy default).
   """
   ...

@overload
def mesh_query_point(id: uint64, point: vec3, max_dist: float32, inside: float32, face: int32, bary_u: float32, bary_v: float32) -> bool:
   """
   Computes the closest point on the mesh with identifier `id` to the given point in space. Returns ``True`` if a point < ``max_dist`` is found.

      :param id: The mesh identifier
      :param point: The point in space to query
      :param max_dist: Mesh faces above this distance will not be considered by the query
      :param inside: Returns a value < 0 if query point is inside the mesh, >=0 otherwise. Note that mesh must be watertight for this to be robust
      :param face: Returns the index of the closest face
      :param bary_u: Returns the barycentric u coordinate of the closest point
      :param bary_v: Retruns the barycentric v coordinate of the closest point
   """
   ...

@overload
def mesh_query_ray(id: uint64, start: vec3, dir: vec3, max_t: float32, t: float32, bary_u: float32, bary_v: float32, sign: float32, normal: vec3, face: int32) -> bool:
   """
   Computes the closest ray hit on the mesh with identifier `id`, returns ``True`` if a point < ``max_t`` is found.

      :param id: The mesh identifier
      :param start: The start point of the ray
      :param dir: The ray direction (should be normalized)
      :param max_t: The maximum distance along the ray to check for intersections
      :param t: Returns the distance of the closest hit along the ray
      :param bary_u: Returns the barycentric u coordinate of the closest hit
      :param bary_v: Returns the barycentric v coordinate of the closest hit
      :param sign: Returns a value > 0 if the hit ray hit front of the face, returns < 0 otherwise
      :param normal: Returns the face normal
      :param face: Returns the index of the hit face
   """
   ...

@overload
def mesh_query_aabb(id: uint64, lower: vec3, upper: vec3) -> mesh_query_aabb_t:
   """
   Construct an axis-aligned bounding box query against a mesh object. This query can be used to iterate over all triangles
      inside a volume. Returns an object that is used to track state during mesh traversal.
    
      :param id: The mesh identifier
      :param lower: The lower bound of the bounding box in mesh space
      :param upper: The upper bound of the bounding box in mesh space
   """
   ...

@overload
def mesh_query_aabb_next(query: mesh_query_aabb_t, index: int32) -> bool:
   """
   Move to the next triangle overlapping the query bounding box. The index of the current face is stored in ``index``, returns ``False``
      if there are no more overlapping triangles.
   """
   ...

@overload
def mesh_eval_position(id: uint64, face: int32, bary_u: float32, bary_v: float32) -> vec3:
   """
   Evaluates the position on the mesh given a face index, and barycentric coordinates.
   """
   ...

@overload
def mesh_eval_velocity(id: uint64, face: int32, bary_u: float32, bary_v: float32) -> vec3:
   """
   Evaluates the velocity on the mesh given a face index, and barycentric coordinates.
   """
   ...

@overload
def hash_grid_query(id: uint64, point: vec3, max_dist: float32) -> hash_grid_query_t:
   """
   Construct a point query against a hash grid. This query can be used to iterate over all neighboring points withing a 
      fixed radius from the query point. Returns an object that is used to track state during neighbor traversal.
   """
   ...

@overload
def hash_grid_query_next(query: hash_grid_query_t, index: int32) -> bool:
   """
   Move to the next point in the hash grid query. The index of the current neighbor is stored in ``index``, returns ``False``
      if there are no more neighbors.
   """
   ...

@overload
def hash_grid_point_id(id: uint64, index: int32) -> int:
   """
   Return the index of a point in the grid, this can be used to re-order threads such that grid 
      traversal occurs in a spatially coherent order.
   """
   ...

@overload
def intersect_tri_tri(v0: vec3, v1: vec3, v2: vec3, u0: vec3, u1: vec3, u2: vec3) -> int:
   """
   Tests for intersection between two triangles (v0, v1, v2) and (u0, u1, u2) using Moller's method. Returns > 0 if triangles intersect.
   """
   ...

@overload
def mesh_eval_face_normal(id: uint64, face: int32) -> vec3:
   """
   Evaluates the face normal the mesh given a face index.
   """
   ...

@overload
def mesh_get_point(id: uint64, index: int32) -> vec3:
   """
   Returns the point of the mesh given a index.
   """
   ...

@overload
def mesh_get_velocity(id: uint64, index: int32) -> vec3:
   """
   Returns the velocity of the mesh given a index.
   """
   ...

@overload
def mesh_get_index(id: uint64, index: int32) -> int:
   """
   Returns the point-index of the mesh given a face-vertex index.
   """
   ...

@overload
def closest_point_edge_edge(p1: vec3, q1: vec3, p2: vec3, q2: vec3, epsilon: float32) -> vec3:
   """
   Finds the closest points between two edges. Returns barycentric weights to the points on each edge, as well as the closest distance between the edges.

      :param p1: First point of first edge
      :param q1: Second point of first edge
      :param p2: First point of second edge
      :param q2: Second point of second edge
      :param epsilon: Zero tolerance for determining if points in an edge are degenerate.
      :param out: vec3 output containing (s,t,d), where `s` in [0,1] is the barycentric weight for the first edge, `t` is the barycentric weight for the second edge, and `d` is the distance between the two edges at these two closest points.
   """
   ...

@overload
def volume_sample_f(id: uint64, uvw: vec3, sampling_mode: int32) -> float:
   """
   Sample the volume given by ``id`` at the volume local-space point ``uvw``. Interpolation should be ``wp.Volume.CLOSEST``, or ``wp.Volume.LINEAR.``
   """
   ...

@overload
def volume_lookup_f(id: uint64, i: int32, j: int32, k: int32) -> float:
   """
   Returns the value of voxel with coordinates ``i``, ``j``, ``k``, if the voxel at this index does not exist this function returns the background value
   """
   ...

@overload
def volume_sample_v(id: uint64, uvw: vec3, sampling_mode: int32) -> vec3:
   """
   Sample the vector volume given by ``id`` at the volume local-space point ``uvw``. Interpolation should be ``wp.Volume.CLOSEST``, or ``wp.Volume.LINEAR.``
   """
   ...

@overload
def volume_lookup_v(id: uint64, i: int32, j: int32, k: int32) -> vec3:
   """
   Returns the vector value of voxel with coordinates ``i``, ``j``, ``k``, if the voxel at this index does not exist this function returns the background value
   """
   ...

@overload
def volume_sample_i(id: uint64, uvw: vec3) -> int:
   """
   Sample the int32 volume given by ``id`` at the volume local-space point ``uvw``. 
   """
   ...

@overload
def volume_lookup_i(id: uint64, i: int32, j: int32, k: int32) -> int:
   """
   Returns the int32 value of voxel with coordinates ``i``, ``j``, ``k``, if the voxel at this index does not exist this function returns the background value
   """
   ...

@overload
def volume_index_to_world(id: uint64, uvw: vec3) -> vec3:
   """
   Transform a point defined in volume index space to world space given the volume's intrinsic affine transformation.
   """
   ...

@overload
def volume_world_to_index(id: uint64, xyz: vec3) -> vec3:
   """
   Transform a point defined in volume world space to the volume's index space, given the volume's intrinsic affine transformation.
   """
   ...

@overload
def volume_index_to_world_dir(id: uint64, uvw: vec3) -> vec3:
   """
   Transform a direction defined in volume index space to world space given the volume's intrinsic affine transformation.
   """
   ...

@overload
def volume_world_to_index_dir(id: uint64, xyz: vec3) -> vec3:
   """
   Transform a direction defined in volume world space to the volume's index space, given the volume's intrinsic affine transformation.
   """
   ...

@overload
def rand_init(seed: int32) -> uint32:
   """
   Initialize a new random number generator given a user-defined seed. Returns a 32-bit integer representing the RNG state.
   """
   ...

@overload
def rand_init(seed: int32, offset: int32) -> uint32:
   """
   Initialize a new random number generator given a user-defined seed and an offset. 
      This alternative constructor can be useful in parallel programs, where a kernel as a whole should share a seed,
      but each thread should generate uncorrelated values. In this case usage should be ``r = rand_init(seed, tid)``
   """
   ...

@overload
def randi(state: uint32) -> int:
   """
   Return a random integer between [0, 2^32)
   """
   ...

@overload
def randi(state: uint32, min: int32, max: int32) -> int:
   """
   Return a random integer between [min, max)
   """
   ...

@overload
def randf(state: uint32) -> float:
   """
   Return a random float between [0.0, 1.0)
   """
   ...

@overload
def randf(state: uint32, min: float32, max: float32) -> float:
   """
   Return a random float between [min, max)
   """
   ...

@overload
def randn(state: uint32) -> float:
   """
   Sample a normal distribution
   """
   ...

@overload
def noise(state: uint32, x: float32) -> float:
   """
   Non-periodic Perlin-style noise in 1d.
   """
   ...

@overload
def noise(state: uint32, xy: vec2) -> float:
   """
   Non-periodic Perlin-style noise in 2d.
   """
   ...

@overload
def noise(state: uint32, xyz: vec3) -> float:
   """
   Non-periodic Perlin-style noise in 3d.
   """
   ...

@overload
def noise(state: uint32, xyzt: vec4) -> float:
   """
   Non-periodic Perlin-style noise in 4d.
   """
   ...

@overload
def pnoise(state: uint32, x: float32, px: int32) -> float:
   """
   Periodic Perlin-style noise in 1d.
   """
   ...

@overload
def pnoise(state: uint32, xy: vec2, px: int32, py: int32) -> float:
   """
   Periodic Perlin-style noise in 2d.
   """
   ...

@overload
def pnoise(state: uint32, xyz: vec3, px: int32, py: int32, pz: int32) -> float:
   """
   Periodic Perlin-style noise in 3d.
   """
   ...

@overload
def pnoise(state: uint32, xyzt: vec4, px: int32, py: int32, pz: int32, pt: int32) -> float:
   """
   Periodic Perlin-style noise in 4d.
   """
   ...

@overload
def curlnoise(state: uint32, xy: vec2) -> vec2:
   """
   Divergence-free vector field based on the gradient of a Perlin noise function.
   """
   ...

@overload
def curlnoise(state: uint32, xyz: vec3) -> vec3:
   """
   Divergence-free vector field based on the curl of three Perlin noise functions.
   """
   ...

@overload
def curlnoise(state: uint32, xyzt: vec4) -> vec3:
   """
   Divergence-free vector field based on the curl of three Perlin noise functions.
   """
   ...

@overload
def printf():
   """
   Allows printing formatted strings, using C-style format specifiers.
   """
   ...

@overload
def tid() -> int:
   """
   Return the current thread index. Note that this is the *global* index of the thread in the range [0, dim) 
      where dim is the parameter passed to kernel launch.
   """
   ...

@overload
def tid() -> Tuple[int, int]:
   """
   Return the current thread indices for a 2d kernel launch. Use ``i,j = wp.tid()`` syntax to retrieve the coordinates inside the kernel thread grid.
   """
   ...

@overload
def tid() -> Tuple[int, int, int]:
   """
   Return the current thread indices for a 3d kernel launch. Use ``i,j,k = wp.tid()`` syntax to retrieve the coordinates inside the kernel thread grid.
   """
   ...

@overload
def tid() -> Tuple[int, int, int, int]:
   """
   Return the current thread indices for a 4d kernel launch. Use ``i,j,k,l = wp.tid()`` syntax to retrieve the coordinates inside the kernel thread grid.
   """
   ...

@overload
def select(cond: bool, arg1: Any, arg2: Any):
   """
   Select between two arguments, if cond is false then return ``arg1``, otherwise return ``arg2``
   """
   ...

@overload
def atomic_add(a: array[Any], i: int32, value: Any):
   """
   Atomically add ``value`` onto the array at location given by index.
   """
   ...

@overload
def atomic_add(a: array[Any], i: int32, j: int32, value: Any):
   """
   Atomically add ``value`` onto the array at location given by indices.
   """
   ...

@overload
def atomic_add(a: array[Any], i: int32, j: int32, k: int32, value: Any):
   """
   Atomically add ``value`` onto the array at location given by indices.
   """
   ...

@overload
def atomic_add(a: array[Any], i: int32, j: int32, k: int32, l: int32, value: Any):
   """
   Atomically add ``value`` onto the array at location given by indices.
   """
   ...

@overload
def atomic_sub(a: array[Any], i: int32, value: Any):
   """
   Atomically subtract ``value`` onto the array at location given by index.
   """
   ...

@overload
def atomic_sub(a: array[Any], i: int32, j: int32, value: Any):
   """
   Atomically subtract ``value`` onto the array at location given by indices.
   """
   ...

@overload
def atomic_sub(a: array[Any], i: int32, j: int32, k: int32, value: Any):
   """
   Atomically subtract ``value`` onto the array at location given by indices.
   """
   ...

@overload
def atomic_sub(a: array[Any], i: int32, j: int32, k: int32, l: int32, value: Any):
   """
   Atomically subtract ``value`` onto the array at location given by indices.
   """
   ...

@overload
def index(a: vec2, i: int32) -> float:
   """

   """
   ...

@overload
def index(a: vec3, i: int32) -> float:
   """

   """
   ...

@overload
def index(a: vec4, i: int32) -> float:
   """

   """
   ...

@overload
def index(a: quat, i: int32) -> float:
   """

   """
   ...

@overload
def index(a: mat22, i: int32) -> vec2:
   """

   """
   ...

@overload
def index(a: mat22, i: int32, j: int32) -> float:
   """

   """
   ...

@overload
def index(a: mat33, i: int32) -> vec3:
   """

   """
   ...

@overload
def index(a: mat33, i: int32, j: int32) -> float:
   """

   """
   ...

@overload
def index(a: mat44, i: int32) -> vec4:
   """

   """
   ...

@overload
def index(a: mat44, i: int32, j: int32) -> float:
   """

   """
   ...

@overload
def expect_eq(arg1: int8, arg2: int8):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: uint8, arg2: uint8):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: int16, arg2: int16):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: uint16, arg2: uint16):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: int32, arg2: int32):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: uint32, arg2: uint32):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: int64, arg2: int64):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: uint64, arg2: uint64):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: float16, arg2: float16):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: float32, arg2: float32):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: float64, arg2: float64):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: vec2, arg2: vec2):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: vec3, arg2: vec3):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: vec4, arg2: vec4):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: mat22, arg2: mat22):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: mat33, arg2: mat33):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: mat44, arg2: mat44):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: quat, arg2: quat):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: transform, arg2: transform):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: spatial_vector, arg2: spatial_vector):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: spatial_matrix, arg2: spatial_matrix):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def lerp(a: float16, b: float16, t: float32) -> float16:
   """
   Linearly interpolate two values a and b using factor t, computed as ``a*(1-t) + b*t``
   """
   ...

@overload
def lerp(a: float32, b: float32, t: float32) -> float32:
   """
   Linearly interpolate two values a and b using factor t, computed as ``a*(1-t) + b*t``
   """
   ...

@overload
def lerp(a: float64, b: float64, t: float32) -> float64:
   """
   Linearly interpolate two values a and b using factor t, computed as ``a*(1-t) + b*t``
   """
   ...

@overload
def lerp(a: vec2, b: vec2, t: float32) -> vec2:
   """
   Linearly interpolate two values a and b using factor t, computed as ``a*(1-t) + b*t``
   """
   ...

@overload
def lerp(a: vec3, b: vec3, t: float32) -> vec3:
   """
   Linearly interpolate two values a and b using factor t, computed as ``a*(1-t) + b*t``
   """
   ...

@overload
def lerp(a: vec4, b: vec4, t: float32) -> vec4:
   """
   Linearly interpolate two values a and b using factor t, computed as ``a*(1-t) + b*t``
   """
   ...

@overload
def lerp(a: mat22, b: mat22, t: float32) -> mat22:
   """
   Linearly interpolate two values a and b using factor t, computed as ``a*(1-t) + b*t``
   """
   ...

@overload
def lerp(a: mat33, b: mat33, t: float32) -> mat33:
   """
   Linearly interpolate two values a and b using factor t, computed as ``a*(1-t) + b*t``
   """
   ...

@overload
def lerp(a: mat44, b: mat44, t: float32) -> mat44:
   """
   Linearly interpolate two values a and b using factor t, computed as ``a*(1-t) + b*t``
   """
   ...

@overload
def lerp(a: quat, b: quat, t: float32) -> quat:
   """
   Linearly interpolate two values a and b using factor t, computed as ``a*(1-t) + b*t``
   """
   ...

@overload
def lerp(a: transform, b: transform, t: float32) -> transform:
   """
   Linearly interpolate two values a and b using factor t, computed as ``a*(1-t) + b*t``
   """
   ...

@overload
def lerp(a: spatial_vector, b: spatial_vector, t: float32) -> spatial_vector:
   """
   Linearly interpolate two values a and b using factor t, computed as ``a*(1-t) + b*t``
   """
   ...

@overload
def lerp(a: spatial_matrix, b: spatial_matrix, t: float32) -> spatial_matrix:
   """
   Linearly interpolate two values a and b using factor t, computed as ``a*(1-t) + b*t``
   """
   ...

@overload
def expect_near(arg1: float32, arg2: float32, tolerance: float32):
   """
   Prints an error to stdout if arg1 and arg2 are not closer than tolerance in magnitude
   """
   ...

@overload
def expect_near(arg1: vec3, arg2: vec3, tolerance: float32):
   """
   Prints an error to stdout if any element of arg1 and arg2 are not closer than tolerance in magnitude
   """
   ...

@overload
def add(x: int32, y: int32) -> int:
   """

   """
   ...

@overload
def add(x: float32, y: float32) -> float:
   """

   """
   ...

@overload
def add(x: vec2, y: vec2) -> vec2:
   """

   """
   ...

@overload
def add(x: vec3, y: vec3) -> vec3:
   """

   """
   ...

@overload
def add(x: vec4, y: vec4) -> vec4:
   """

   """
   ...

@overload
def add(x: quat, y: quat) -> quat:
   """

   """
   ...

@overload
def add(x: mat22, y: mat22) -> mat22:
   """

   """
   ...

@overload
def add(x: mat33, y: mat33) -> mat33:
   """

   """
   ...

@overload
def add(x: mat44, y: mat44) -> mat44:
   """

   """
   ...

@overload
def add(x: spatial_vector, y: spatial_vector) -> spatial_vector:
   """

   """
   ...

@overload
def add(x: spatial_matrix, y: spatial_matrix) -> spatial_matrix:
   """

   """
   ...

@overload
def sub(x: int32, y: int32) -> int:
   """

   """
   ...

@overload
def sub(x: float32, y: float32) -> float:
   """

   """
   ...

@overload
def sub(x: vec2, y: vec2) -> vec2:
   """

   """
   ...

@overload
def sub(x: vec3, y: vec3) -> vec3:
   """

   """
   ...

@overload
def sub(x: vec4, y: vec4) -> vec4:
   """

   """
   ...

@overload
def sub(x: mat22, y: mat22) -> mat22:
   """

   """
   ...

@overload
def sub(x: mat33, y: mat33) -> mat33:
   """

   """
   ...

@overload
def sub(x: mat44, y: mat44) -> mat44:
   """

   """
   ...

@overload
def sub(x: spatial_vector, y: spatial_vector) -> spatial_vector:
   """

   """
   ...

@overload
def sub(x: spatial_matrix, y: spatial_matrix) -> spatial_matrix:
   """

   """
   ...

@overload
def mul(x: int32, y: int32) -> int:
   """

   """
   ...

@overload
def mul(x: float32, y: float32) -> float:
   """

   """
   ...

@overload
def mul(x: float32, y: vec2) -> vec2:
   """

   """
   ...

@overload
def mul(x: float32, y: vec3) -> vec3:
   """

   """
   ...

@overload
def mul(x: float32, y: vec4) -> vec4:
   """

   """
   ...

@overload
def mul(x: float32, y: quat) -> quat:
   """

   """
   ...

@overload
def mul(x: float32, y: mat22) -> mat22:
   """

   """
   ...

@overload
def mul(x: float32, y: mat33) -> mat33:
   """

   """
   ...

@overload
def mul(x: float32, y: mat44) -> mat44:
   """

   """
   ...

@overload
def mul(x: vec2, y: float32) -> vec2:
   """

   """
   ...

@overload
def mul(x: vec3, y: float32) -> vec3:
   """

   """
   ...

@overload
def mul(x: vec4, y: float32) -> vec4:
   """

   """
   ...

@overload
def mul(x: quat, y: float32) -> quat:
   """

   """
   ...

@overload
def mul(x: quat, y: quat) -> quat:
   """

   """
   ...

@overload
def mul(x: mat22, y: float32) -> mat22:
   """

   """
   ...

@overload
def mul(x: mat22, y: vec2) -> vec2:
   """

   """
   ...

@overload
def mul(x: mat22, y: mat22) -> mat22:
   """

   """
   ...

@overload
def mul(x: mat33, y: float32) -> mat33:
   """

   """
   ...

@overload
def mul(x: mat33, y: vec3) -> vec3:
   """

   """
   ...

@overload
def mul(x: mat33, y: mat33) -> mat33:
   """

   """
   ...

@overload
def mul(x: mat44, y: float32) -> mat44:
   """

   """
   ...

@overload
def mul(x: mat44, y: vec4) -> vec4:
   """

   """
   ...

@overload
def mul(x: mat44, y: mat44) -> mat44:
   """

   """
   ...

@overload
def mul(x: spatial_vector, y: float32) -> spatial_vector:
   """

   """
   ...

@overload
def mul(x: spatial_matrix, y: spatial_matrix) -> spatial_matrix:
   """

   """
   ...

@overload
def mul(x: spatial_matrix, y: spatial_vector) -> spatial_vector:
   """

   """
   ...

@overload
def mul(x: transform, y: transform) -> transform:
   """

   """
   ...

@overload
def mod(x: int32, y: int32) -> int:
   """

   """
   ...

@overload
def mod(x: float32, y: float32) -> float:
   """

   """
   ...

@overload
def div(x: int32, y: int32) -> int:
   """

   """
   ...

@overload
def div(x: float32, y: float32) -> float:
   """

   """
   ...

@overload
def div(x: vec2, y: float32) -> vec2:
   """

   """
   ...

@overload
def div(x: vec3, y: float32) -> vec3:
   """

   """
   ...

@overload
def div(x: vec4, y: float32) -> vec4:
   """

   """
   ...

@overload
def floordiv(x: int32, y: int32) -> int:
   """

   """
   ...

@overload
def floordiv(x: float32, y: float32) -> float:
   """

   """
   ...

@overload
def neg(x: int32) -> int:
   """

   """
   ...

@overload
def neg(x: float32) -> float:
   """

   """
   ...

@overload
def neg(x: vec2) -> vec2:
   """

   """
   ...

@overload
def neg(x: vec3) -> vec3:
   """

   """
   ...

@overload
def neg(x: vec4) -> vec4:
   """

   """
   ...

@overload
def neg(x: quat) -> quat:
   """

   """
   ...

@overload
def neg(x: mat33) -> mat33:
   """

   """
   ...

@overload
def neg(x: mat44) -> mat44:
   """

   """
   ...

@overload
def unot(b: bool) -> bool:
   """

   """
   ...
