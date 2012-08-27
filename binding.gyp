{
	"targets": [
		{
			'target_name': 'msgpackBinding',
			'sources': [
				'src/msgpack.cc',
			],
			'include_dirs': [
				'deps/msgpack'
			],
			'dependencies': [
				'deps/msgpack/msgpack.gyp:libmsgpack'
			],
			'cflags_cc': [
					'-Wall',
					'-O3'
				],
				'cflags': [
					'-Wall',
					'-O3'
				],
				'cflags!': ['-fno-exceptions'],
				'cflags_cc!': ['-fno-exceptions'],
				'conditions': [
					['OS=="mac"', {
						'xcode_settings': {
							'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
						}

					}]
				]
			},
	]
}
