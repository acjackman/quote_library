require 'spec_helper'

describe Author do
  
  before { @author = Author.new(prefix: "a", firstname: "b", middlename: "c",
                                lastname: "d", suffix: "e", 
                                birthdate: Date.today, deathdate: Date.today,
                                birthdateyear: false, deathdateyear: false,
                                profession: "Job", bio: "Lorem ipsum", 
                                notes: "Lorem ipsum") }
  
  subject { @author }
  
  it { should respond_to(:bio) }
  it { should respond_to(:birthdate) }
  it { should respond_to(:birthdateyear) }
  it { should respond_to(:deathdate) }
  it { should respond_to(:deathdateyear) }
  it { should respond_to(:firstname) }
  it { should respond_to(:lastname) }
  it { should respond_to(:middlename) }
  it { should respond_to(:notes) }
  it { should respond_to(:prefix) }
  it { should respond_to(:profession) }
  it { should respond_to(:suffix) }
  
  it { should be_valid }
  
  
  describe "when it has no last name" do
    before { @author.lastname = "" }
    it { should_not be_valid }
  end
end
