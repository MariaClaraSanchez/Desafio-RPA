import yaml


class Config:
    @staticmethod
    def get_config() -> dict:
        with open("jaguara.yaml", "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
            return data
