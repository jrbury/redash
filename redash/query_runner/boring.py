from redash.query_runner import BaseQueryRunner, register


class Boring(BaseQueryRunner):
    noop_query = "SELECT 1"

    @classmethod
    def enabled(cls):
        return True

    @classmethod
    def configuration_schema(cls):
        return {
            "type": "object",
            "properties": {
                "user": {
                    "type": "string"
                },
                "password": {
                    "type": "string"
                },
                "database": {
                    "type": "string"
                }
            },
            "required": ["user", "password", "database"],
            "secret": ["password"]
        }

    def run_query(self, query, user):
        pass


register(Boring)
