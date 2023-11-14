from airflow.models.baseoperator import BaseOperator
from utils import page_saver
from airflow.utils.decorators import apply_defaults


class TestGetterOperator(BaseOperator):
    @apply_defaults
    def __init__(self, url, path, **kwargs):
        super().__init__(**kwargs)
        self.url = url
        self.path = path

    def execute(self, context):
        page_saver(self.url, self.path)
