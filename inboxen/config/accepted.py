from config import settings
from lamson.routing import Router
from lamson.server import QueueReceiver
import logging
import logging.config

logging.config.fileConfig("config/logging.conf")

settings.receiver = QueueReceiver(settings.accepted_queue_dir,
                            **settings.accepted_queue_opts_out)

Router.defaults(**settings.router_defaults)
Router.load(settings.out_handlers)
Router.RELOAD=True
Router.UNDELIVERABLE_QUEUE=queue.Queue("run/undeliverable")