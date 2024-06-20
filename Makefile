GIT_COMMIT ?= $(shell git rev-parse --short HEAD || echo "0.0.0")
REGISTRY := registry.cn-beijing.aliyuncs.com/liteyun-labs
IMAGE_NAME := $(REGISTRY)/cert-update:$(GIT_COMMIT)

build:
	@docker build -t $(IMAGE_NAME) -f Dockerfile .
	