import os
import json

apiId = ''

# Create dictionary of function names from AWS Appsync
cmdListFunctions = 'aws appsync list-functions --api-id ' + apiId
rawFunctionList = os.popen(cmdListFunctions).read()
functionsList = json.loads(rawFunctionList)
functions = {}

for function in functionsList['functions']:
    functions[function['name']] = function['functionId']

# Iterate through files in PipelineJsons dir
for fileName in os.listdir('./PipelineJsons'):
    with open('./PipelineJsons/' + fileName, 'r') as f:
        parsed_json = json.load(f)

    with open('./Resolvers/' + parsed_json['requestMappingTemplate'], 'r') as f:
        requestMappingTemplate = f.read()

    with open('./Resolvers/' + parsed_json['responseMappingTemplate'], 'r') as f:
        responseMappingTemplate = f.read()

    pipelineConfig = parsed_json['pipelineConfig']
    pipelineString = ''
    for pipeline in pipelineConfig['functions']:
        pipelineString = pipelineString + functions[pipeline] + ','
    pipelineString = pipelineString[:-1]

    apiId = parsed_json['apiId']
    typeName = parsed_json['typeName']
    fieldName = parsed_json['fieldName']
    kind = parsed_json['kind']

    cmdUpdateResolver = 'aws appsync update-resolver --api-id ' + apiId + ' --type-name ' \
        + typeName + ' --field-name ' + fieldName + ' --request-mapping-template ' \
        + "'" + requestMappingTemplate + "'" + ' --response-mapping-template ' \
        + "'" + responseMappingTemplate + "'" + ' --kind ' + kind + ' --pipeline-config functions=' \
        + pipelineString

    os.system(cmdUpdateResolver)