#!/usr/bin/env python

import yaml
import csv

from bl import all_pull_requests, all_comments


if __name__ == '__main__':
    with open("config.yaml", "r") as stream:
        try:
            configs = yaml.safe_load(stream)

            print("=====> your configuration: \n {}".format(configs))
            user_token = configs['user-token']
            user_id = configs['user-id']
            repos = configs['githubs']
            created_at = configs['created-at']
            is_export_csv = configs['csv']
            all_prs = []
            pr_comments = {}

            print("=====> your pull requests:")
            for repo in repos:
                prs = all_pull_requests(
                    user_token, user_id, repos=repo, created_at=created_at)
                all_prs += prs
            print(all_prs)

            print("=====> your comments:")
            for pr in all_prs:
                comments = all_comments(
                    user_token, pull_request=pr)
                pr_comments[pr.html_url] = comments
            print(pr_comments)

            if is_export_csv == True:
                print("======> dump report to out.csv")
                with open('./out.csv', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Name', 'comments'])
                    for key, values in pr_comments.items():
                        writer.writerow(
                            [key, len(pr_comments[key])])

        except yaml.YAMLError as exc:
            print(exc)
        except Exception as exc:
            print(exc)
