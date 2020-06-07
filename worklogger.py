import configparser


# https://github.com/OpenPecha/openpecha-bot/commits?author=10zinten&since=2020-06-03&until=2020-06-04
class Config:
    def __init__(self, fn="config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(fn)
        self.repos = []

    @property
    def gh_username(self):
        return self.config["DEFAULT"]["github_username"]

    def add_repos(self, section):
        repo_url_template = "https://github.com/{}/{}/commits?author={}"
        loc = self.gh_username if section == "DEFAULT" else section
        for repo in self.config[section]["repos"].split(" "):
            repo_url = repo_url_template.format(loc, repo, self.gh_username)
            self.repos.append(repo_url)

    def get_repos(self):
        self.add_repos("DEFAULT")
        for section in self.config.sections():
            self.add_repos(section)
        return self.repos


if __name__ == "__main__":
    config = Config()
    repos = config.get_repos()
    print(repos)
