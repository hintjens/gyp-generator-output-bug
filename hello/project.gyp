{
  'targets': [
    {
      'target_name': 'hello',
      'type': 'executable',
      'sources': [ 'hello.c' ],
      'dependencies': [
        '../world/project.gyp:world',
      ]
    }
  ]
}
