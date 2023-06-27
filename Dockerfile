ARG GCC_VERSION

FROM gcc:${GCC_VERSION} as builder
ARG IS_REMOTE="http://0.0.0.0:9300"

WORKDIR /opt/is
COPY scripts scripts
COPY recipes recipes

# install required packages, cmake and setup conan 
RUN ./scripts/bootstrap.sh

# activate virtual environment to use conan
ENV PATH="/opt/is/.venv/bin:${PATH}"

# create all packages
RUN ./scripts/create_packages.sh && \
    conan remote add is ${IS_REMOTE}