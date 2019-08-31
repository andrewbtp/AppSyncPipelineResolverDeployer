# AppSync Pipeline Resolver Deployment

## Purpose
Amplify is great. Amplify with complex APIs is not so great.
When pushing API updates in Amplify, Amplify clears any pipeline resolvers that have been set.
This makes it easy to re-deploy pipeline resolvers.

## How to use it
You'll need Python 3 and a folder structure like this repo.
1. Stick the AppSync API ID in `deployResolverPipelines.py, line 4`
2. Build request and response templates in `Resolvers` or use my standard (plain) templates
3. Build functions through the AppSync UI
4. Build pipeline JSONs in `PipelineJsons`. Check out my sample JSON in `PipelineJsons`.
Note: The script converts function names to function ids, so ensure you don't have duplicate function names in AppSync!
5. Run the script with `python3 deployResolverPipelines.py`

## FAQs
**New features?**

I'd love to be able to version control my functions,
so deploying function code from this repo is the most likely future feature.

**Why aren't you using boto3?**

Because this was quick and dirty.

**Why aren't you using Cloud Formation Templates?**

I got the command line commands working before I thought to look into CFTs. Maybe I'll change this to use CFTs in the future.

**Are you going to add support for X?**

Probably not unless I need it. Feel free to make a PR.

**Amplify now supports pipeline resolvers, what's the point of this?**

You're living in the future, my friend. Amplify had 0 support for deploying pipeline resolvers in August 2019.
