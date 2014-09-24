# Generated from colored-1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name colored
%global rubyabi 1.8
%define _unpackaged_files_terminate_build 0

Name: rubygem-%{gem_name}
Version: 1.2
Release: 1%{?dist}
Summary: Add some color to your life
Group: Development/Languages
License: Internal
URL: http://github.com/defunkt/colored
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
>> puts "this is red".red
>> puts "this is red with a blue background (read: ugly)".red_on_blue
>> puts "this is red with an underline".red.underline
>> puts "this is really bold and really blue".bold.blue
>> logger.debug "hey this is broken!".red_on_yellow     # in rails
>> puts Color.red "This is red" # but this part is mostly untested.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Wed Sep 24 2014 root <root@r10k-centos6-build> - 1.2-1
- Initial package
