import os

HOME = os.environ['HOME']
print('Home directory', HOME)

configs = [
    {
    "start_dir": [
      f'{HOME}/Downloads/',
      f'{HOME}/Desktop/'
    ],
    "rules" :[
        { 
          "conditions": { 
          "any": [
            { 
              "name": "target_file_name",
              "operator": "contains",
              "value": 'Screen Shot',
            }
          ]
      },
      "actions": [
          { 
            "name": "move_to_backup",
            "params": {
              "target_dir": f'{HOME}/Desktop/backup'
            },
          },
        ]
      },
      {
            "conditions": { 
            "any": [
              { 
                "name": "target_file_name",
                "operator": "ends_with",
                "value": '.pdf',
              }
            ]
        },
        "actions": [
            { 
              "name": "move_to_backup",
              "params": {
                "target_dir": f'{HOME}/Desktop/backup/pdfs'
              },
            },
        ],
      },
      {
            "conditions": { 
            "any": [
              { 
                "name": "target_file_name",
                "operator": "ends_with",
                "value": '.stl',
              },
              { 
                "name": "target_file_name",
                "operator": "ends_with",
                "value": '.gcode',
              }
            ]
        },
        "actions": [
            { 
              "name": "delete_dir",
              "params": {},
            },
        ],
      }
    ]
  }
]
