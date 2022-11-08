tensorboard-dev:
	docker build -t tensorflow/tensorboard tensorboard && \
	docker run \
		-p 6006:6006 \
		-v tensorboard:/tensorboard/tensorboard \
		-v logs:/logdir \
		tensorflow/tensorboard \
		ibazel run tensorboard:dev -- --logdir /logdir --bind_all
