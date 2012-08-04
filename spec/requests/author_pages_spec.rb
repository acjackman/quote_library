require 'spec_helper'

describe "Author pages" do

  subject { page }

  describe "show" do
    let(:author) { FactoryGirl.create(:author) } # Create Author
    before { visit author_path(author) }
    
    describe "page" do
      it { should have_selector('title', text: full_title(author.full_name)) }
      it { should have_selector('h1',    text: author.full_name) }
    end
  end

  describe "create page" do
    before { visit new_author_path }

    let(:submit) { "Create author" }

    it { should have_selector('h1',    text: 'New Author') }
    it { should have_selector('title', text: full_title('New Author')) }
    
    describe "with invalid information" do
      it "should not create a author" do
        expect { click_button submit }.not_to change(Author, :count)
      end
    end
    
    describe "with valid information" do
      before do
        fill_in "Prefix",       with: "p"
        fill_in "First Name",   with: "f"
        fill_in "Middle Name",  with: "m"
        fill_in "Last Name",    with: "l"
        fill_in "Suffix",       with: "s"
      end

      it "should create a author" do
        expect { click_button submit }.to change(Author, :count).by(1)
      end
    end
  end
  
  describe "edit" do
    let(:author) { FactoryGirl.create(:author) }
    before { visit edit_author_path(author) }

    describe "page" do
      it { should have_selector('h1',    text: ("Edit " + author.full_name)) }
      it { should have_selector('title', text: ("Edit " + author.full_name)) }
    end

    describe "with invalid information" do
      before do
        fill_in "Last Name",    with: " "
        click_button "Save changes"
      end

      it { should have_content('error') }
      it { should have_selector('h1',    text: ("Edit " + author.full_name)) }
      it { should have_selector('title', text: ("Edit " + author.full_name)) }
    end
    
    describe "with valid information" do
      let(:new_prefix)     { "z" }
      let(:new_firstname)  { "y" }
      let(:new_middlename) { "x" }
      let(:new_lastname)   { "w" }
      let(:new_suffix)     { "v" }
      before do
        fill_in "Prefix",       with: new_prefix
        fill_in "First Name",   with: new_firstname
        fill_in "Middle Name",  with: new_middlename
        fill_in "Last Name",    with: new_lastname
        fill_in "Suffix",       with: new_suffix
        click_button "Save changes"
      end
      
      it { should have_selector('title', text: author.reload.full_name ) }
      it { should have_selector('div.alert.alert-success') }
      specify { author.reload.prefix.should     == new_prefix }
      specify { author.reload.firstname.should  == new_firstname }
      specify { author.reload.middlename.should == new_middlename }
      specify { author.reload.lastname.should   == new_lastname }
      specify { author.reload.suffix.should     == new_suffix }
    end
  end
end


