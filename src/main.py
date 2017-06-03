from src.queue.celery_broker import celeryInstance

if __name__ == "__main__":
    argv = [
        'worker',
        '--loglevel=info',
    ]
    celeryInstance.worker_main(argv)