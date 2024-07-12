import os
from template import asset_template

class AssetWerkzeug:
    @staticmethod
    def create_asset_file(tag, path):
        """
        Create an asset file with the given tag and path.

        Args:
            tag (str): The tag to be used in the asset file.
            path (str): The path where the asset file will be saved.

        Returns:
            None

        This function creates an asset file with the given tag and path. The asset file is a text file
        containing entity definitions. Each entity definition has a clone, name, pdxmesh, and attach
        fields. The clone field specifies the entity to clone, the name field specifies the name of the
        entity, the pdxmesh field specifies the mesh to use, and the attach field specifies the attachments
        to use. The attachments are specified as a list of dictionaries, each dictionary containing a name
        and a node name. The function uses string formatting to replace the {tag} placeholder in the template
        with the given tag. The resulting asset file is saved to the given path with a filename generated using
        """
        template = asset_template.format(tag=tag)
        filename = 'zzz_{}_units_generated.asset'.format(tag)
        with open(os.path.join(path, filename), 'w') as f:
            f.write(template)
