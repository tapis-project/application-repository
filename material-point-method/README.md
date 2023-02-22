# Material Point Method (mpm)

The High-Performance Computing (HPC) enabled CB-Geo MPM code; source is available 
on [GitHub](https://github.com/cb-geo/mpm).

Please refer to [CB-Geo MPM Documentation](https://mpm.cb-geo.com/#/user/about) for information 
on running the code. The documentation also includes the MPM theory.


# Using the mpm Applications

Multiple mpm Tapis applications are defined in this repository, including:

 * ``mpm-docker`` -- Docker container version of mpm, good for small examples that can be computed on commodity servers.
 * ``mpm-singularity`` -- Singularity container version of mpm, which can be launched on HPC
 systems such as Stampede2 and Frontera.

These two applications above always point to the latest production release of mpm.

We also include two "development" versions of the applications, useful for CI/CD pipelines
and for trying out the most recent updates to mpm. **Note:** These versions may contain
defects.




