require 'spec_helper'

describe "Author pages" do

  subject { page }

  describe "author page" do
    let(:author) { FactoryGirl.create(:author) } # Create Author
    before { visit author_path(author) }
    
    it { should have_selector('title', text: full_title(author.full_name)) }
    it { should have_selector('h1',    text: author.full_name) }
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
end
