from github import Github
import yaml

# credentials.yml contains your usr/repo and PAT created in step 11 above
# So we load the data into a YML object
data = yaml.safe_load(open('credentials.yml'))

# Extract the user and token from the data object
user = data["creds"]["username"]
token = data["creds"]["token"]

# using an access token
g = Github(token)
repo = g.get_repo(user)

#opening the file to write to
myfile = open("output.txt", "w")

# Get all branches you have created for your public repo
branches = repo.get_branches()
for i in branches:
    myfile.write(str(i) + "\n")

# Get all pull requests you have created
pulls = repo.get_pulls(state = 'all')
for i in pulls:
    myfile.write(str(i) + "\n")

# Get a list of commits you have created in your `main` branch.
commit = list(repo.get_commits(sha='main'))
for i in commit:
    myfile.write(str(i) + "\n")

#closing the files
print("Finished")
myfile.close()