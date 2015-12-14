THIS_MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
BUILD_TOP_DIR := $(abspath $(dir ${THIS_MAKEFILE_PATH}))
INSTALL_PREFIX := ${BUILD_TOP_DIR}/install
VERSION_STRING := 3.7

all:
	make depends
	make source
	make rpm

depends:
	yum install -y make curl tar gcc gcc-c++ python m4 autoconf automake libtool zlib-devel libstdc++-devel git rpm-build
	cd /tmp && curl -L "https://cmake.org/files/v3.4/cmake-3.4.1-Linux-x86_64.tar.gz" -o cmake.tar.gz && \
          tar -xzf cmake.tar.gz && cp -r cmake-3.4.1-Linux-x86_64/* /usr/

source:
	git clone --depth=1 http://llvm.org/git/llvm.git llvm
	cd llvm/tools && git clone --depth=1 http://llvm.org/git/clang.git
	cd llvm/projects && git clone --depth=1 http://llvm.org/git/compiler-rt.git
	cd llvm/projects && git clone --depth=1 http://llvm.org/git/openmp.git
	cd llvm/projects && git clone --depth=1 http://llvm.org/git/libcxx.git && git clone http://llvm.org/git/libcxxabi.git
	tar -czf llvm-clang-${VERSION_STRING}.tar.gz llvm

rpm:
	rpmbuild -bb --define "_topdir ${BUILD_TOP_DIR}" --define "version ${VERSION_STRING}" --define "buildroot ${INSTALL_PREFIX}" ${BUILD_TOP_DIR}/llvm-clang.spec

build-llvm:
	mkdir -p build && cd build && cmake  -DCMAKE_INSTALL_PREFIX=${INSTALL_PREFIX}/usr -DCMAKE_BUILD_TYPE=Release ${BUILD_TOP_DIR}/llvm && make -j4

install-llvm:
	cd build && make install

clean:
	rm -rf build
	rm -rf ${INSTALL_PREFIX}

.PHONY: all depends source rpm build-llvm install-llvm clean
