require 'spec_helper'

describe "Static pages" do

  describe "Home page" do

    it "should have the content 'Quote'" do
      visit root_path
      page.should have_content('Quote')
    end
    
    it "should have the base title" do
      visit root_path
      page.should have_selector('title',
                        text: "Adam's Quotes")
    end
    
    it "should not have a custom page title" do
      visit root_path
      page.should_not have_selector('title', text: '| Home')
    end
  end
  
  describe "Help page" do
    
    it "should have the content 'Help'" do
      visit help_path
      page.should have_content('Help')
    end
    
    it "should have the title 'Help'" do
      visit help_path
      page.should have_selector('title',
                    text: "Adam's Quotes | Help")
    end
  end
  
  describe "About page" do
    
    it "should have the content 'About this site'" do
      visit about_path
      page.should have_content('About this site')
    end
    
    it "should have the title 'About'" do
      visit about_path
      page.should have_selector('title',
                    text: "Adam's Quotes | About")
    end
  end
  
  describe "Contact page" do

    it "should have the h1 'Contact'" do
      visit contact_path
      page.should have_selector('h1', text: 'Contact')
    end

    it "should have the title 'Contact'" do
      visit contact_path
      page.should have_selector('title',
                    text: "Adam's Quotes | Contact")
    end
  end
  
end