%global project felix
%global bundle org.apache.felix.shell

Name:           %{project}-shell
Version:        1.4.3
Release:        4%{?dist}
Summary:        Apache Felix Shell Service

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://felix.apache.org
Source0:        http://archive.apache.org/dist/%{project}/%{bundle}-%{version}-source-release.tar.gz

BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: felix-osgi-core
BuildRequires: felix-osgi-compendium
BuildRequires: maven-clean-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: felix-parent


%description
A simple OSGi command shell service.

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{bundle}-%{version}

%pom_remove_plugin org.codehaus.mojo:rat-maven-plugin

%mvn_file : %{project}/%{bundle}

%build
%mvn_build

%install
%mvn_install
 
%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 1.4.3-4
- Migrate away from mvn-rpmbuild (Resolves: #997489)

* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.3-3
- Remove workaround for rpm bug #646523

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.3-2
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 15 2013 Mat Booth <fedora@matbooth.co.uk> - 1.4.3-1
- Update to latest upstream version rhbz #895405.
- Enable tests

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4.2-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 06 2012 Hui Wang <huwang@redhat.com> - 1.4.2-6
- Bug 810214

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 02 2010 Hui Wang <huwang@redhat.com> - 1.4.2-3
- Fix source0
- Remove "rm -rf target/site/api/*"

* Fri Jul 30 2010 Hui Wang <huwang@redhat.com> - 1.4.2-2
- Add LICENSE to javadoc subpackage
- Use upstream source tarball
- Fix directory that owned by other package in files section

* Fri Jun 25 2010 Hui Wang <huwang@redhat.com> - 1.4.2-1
- Initial version of the package
