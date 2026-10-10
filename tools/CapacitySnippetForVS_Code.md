
This snippet script is a custom snippet for **VS Code** editor for creating new capacities script easily :D

The snippet needs to be placed in the `subrunner_main_directory\\.vscode\\capacity_template.code-snippets` file,
where **`subrunner_main_directory`** is the folder containing the `Assets` / `Library` / etc unity folders as well as the `.git` folder also.

Here is the snippet code :

```
{

    // Place your subrunner workspace snippets here. Each snippet is defined under a snippet name and has a scope, prefix, body and

    // description. Add comma separated ids of the languages where the snippet is applicable in the scope field. If scope

    // is left empty or omitted, the snippet gets applied to all languages. The prefix is what is

    // used to trigger the snippet and the body will be expanded and inserted. Possible variables are:

    // $1, \t\t for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders.

    // Placeholders with the same ids are connected.

    // Example:

    // "Print to console": {

    //  "scope": "javascript,typescript",

    //  "prefix": "log",

    //  "body": [

    //      "console.log('$1');",

    //      "\t\t"

    //  ],

    //  "description": "Log output to console"

    // }

    //

    // You can also restrict snippets to specific files using include/exclude patterns:

    // "Test snippet": {

    //  "scope": "javascript,typescript",

    //  "prefix": "test",

    //  "body": "test('$1', () => {\n\t$0\n});",

    //  "include": ["**/*.test.ts", "*.spec.ts"],

    //  "exclude": ["**/temp/*.ts"],

    //  "description": "Insert test block"

    // }

  

    "Capacity": {

        "prefix": [

            "capacity"

        ],

        "body": [

            "using System;",

            "using System.Collections;",

            "using System.Collections.Generic;",

            "using UnityEngine;",

            "",

            "public class ${1:Specific}Capacity : Capacity",

            "{",

            "\t",

            "\t///",

            "\t//",

            "\t/// DATA MANAGEMENT",

            "\t//",

            "\t///",

            "",

  

            "\t// LOAD / UNLOAD DATA",

            "\tpublic override void LoadData(CapacityData data)",

            "\t{",

            "\t\tbase.LoadData(data);",

            "",

            "\t\tif (data is not ${1:Specific}Data specific_data) { return; }",

            "\t\t// load custom data here",

            "\t}",

  

            "\tpublic override void UnloadData()",

            "\t{",

            "\t\t// unload custom data here",

            "",

            "\t\tbase.UnloadData();",

            "\t}",

  

            "",

  

            "\t// GET STATIC DATA",

            "\tpublic override CapacityData GetStaticData()",

            "\t{",

            "\t\t${1:Specific}Data static_data = new ${1:Specific}Data(base.GetStaticData())",

            "\t\t{",

            "\t\t\t// set custom data fields here",

            "\t\t};",

            "",

            "\t\t// set more complicated data fields check here if needed",

            "",

            "\t\treturn static_data;",

            "\t}",

  

            "}",

            "[Serializable] public class ${1:Specific}Data : CapacityData",

            "{",

            "\t// declare custom data fields here",

            "",

            "\t// CONSTRUCTOR",

            "\tpublic ${1:Specific}Data(CapacityData parent) : base(parent) { }",

            "",

            "\t// DUPLICATE",

            "\tpublic override ICapacityData Duplicate()",

            "\t{",

            "\t\treturn new ${1:Specific}Data(base.Duplicate() as CapacityData)",

            "\t\t{",

            "\t\t\t// copy fields here",

            "\t\t};",

            "\t}",

            "",

            "\t// GET DETAILS",

            "\tpublic override string GetDetails()",

            "\t{",

            "\t\tstring details = \"\";",

            "\t\t// add details to the string here",

            "\t\t// ex : details += $\"  - slot color : {slot_color}\\n\";",

            "\t\treturn base.GetDetails() + details;",

            "\t}",

            "}"

        ],

        "description": "Capacity template, including Data class"

    }

}
```