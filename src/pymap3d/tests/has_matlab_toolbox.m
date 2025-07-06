function h = has_matlab_toolbox(name)

addons = matlab.addons.installedAddons();

h = any(ismember(addons.Name, name)) && matlab.addons.isAddonEnabled(name) == 1;

end


