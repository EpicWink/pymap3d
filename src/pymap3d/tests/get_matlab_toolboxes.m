function h = get_matlab_toolboxes()

h = struct(mapping=has_mapping(), aerospace=has_aerospace());

end


function has_map = has_mapping()
addons = matlab.addons.installedAddons();
n = 'Mapping Toolbox';

has_map = any(ismember(addons.Name, n)) && matlab.addons.isAddonEnabled(n) == 1;
end


function has_map = has_aerospace()
addons = matlab.addons.installedAddons();
n = 'Aerospace Toolbox';

has_map = any(ismember(addons.Name, n)) && matlab.addons.isAddonEnabled(n) == 1;
end
