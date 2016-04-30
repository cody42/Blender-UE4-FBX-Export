from . import blender_unreal_fbx_batch_export as plugin
bl_info = {
	"name": "Blender to Unreal FBX Batch Export",
	"author": "Firestack",
	"version": (0, 0, 1),
	"blender": (2, 70, 0),
	"location": "View3D > Toolbar",
	"description": "Temp",
	"warning": "Debug Build",
	"tracker_url": "https://github.com/firestack/Blender-UE4-FBX-Export/issues",
	"category": "Object"
}
	
def register():
	plugin.register()


def unregister():
	plugin.unregister()


if __name__ == '__main__':
	register()